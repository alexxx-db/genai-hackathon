# Databricks notebook source
# MAGIC %md
# MAGIC ### These are boiler plate code to create UC Functions which can be integrated as tools

# COMMAND ----------

# MAGIC  %pip install -qqqq -U -r requirements.txt
# MAGIC  dbutils.library.restartPython()

# COMMAND ----------

from cookbook.config.shared.agent_storage_location import AgentStorageConfig
from cookbook.config.data_pipeline import (
    DataPipelineConfig,
)
from cookbook.databricks_utils import get_table_url
from cookbook.config import load_serializable_config_from_yaml_file

# Load the Agent's storage configuration
data_pipeline_config: DataPipelineConfig = load_serializable_config_from_yaml_file(
    "./configs/data_pipeline_config.yaml"
)


# COMMAND ----------

dbutils.widgets.text("CATALOG", data_pipeline_config.source.uc_catalog_name)
dbutils.widgets.text("SCHEMA", data_pipeline_config.source.uc_schema_name)
dbutils.widgets.text("INDEX_NAME", str(data_pipeline_config.output.vector_index))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create function to gather reviews about the drug

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${CATALOG}.${SCHEMA}.lookup_drug_info(
# MAGIC   drug_name STRING COMMENT 'Name of the drug whose information to look up')
# MAGIC RETURNS TABLE(drugName STRING , condition STRING, review STRING,rating INT, usefulCount int ,date STRING)
# MAGIC COMMENT "Returns the top 10 reviews for a drug (from the drugs_com table), ordered by usefulness"
# MAGIC RETURN SELECT drugName,condition,review,rating,usefulCount,date
# MAGIC   FROM llm_hackathon.raw_data.drugs
# MAGIC   WHERE drugName like concat("%",drug_name,"%")
# MAGIC   ORDER BY usefulCount DESC
# MAGIC   LIMIT 1
# MAGIC
# MAGIC   -- Question summarize the best review for Mirtazapine

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${CATALOG}.${SCHEMA}.lookup_medicine_info(
# MAGIC   medicine_name STRING COMMENT 'Name of the medicine whose information to look up')
# MAGIC RETURNS STRING
# MAGIC COMMENT "Returns concatenated medicine information"
# MAGIC RETURN select concat("name: ",name,
# MAGIC              " ,substitute0: ",COALESCE(substitute0,""),
# MAGIC              " ,use0: ",COALESCE(use0,"")) from llm_hackathon.raw_data.medicine where name like concat("%",lower(medicine_name),"%") LIMIT 1
# MAGIC
# MAGIC   -- Give the side effects of drug Levofloxacin?

# COMMAND ----------

# MAGIC %sql
# MAGIC select  concat("name: ",name,
# MAGIC              " ,substitute0: ",COALESCE(substitute0,""))
# MAGIC   from llm_hackathon.raw_data.medicine LIMIT 1

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${CATALOG}.${SCHEMA}.search_medical_leaflet (
# MAGIC   -- The agent uses this comment to determine how to generate the query string parameter.
# MAGIC   query STRING
# MAGIC   COMMENT 'The query string for searching medical leaflets.'
# MAGIC ) RETURNS TABLE
# MAGIC -- The agent uses this comment to determine when to call this tool. It describes the types of documents and information contained within the index.
# MAGIC COMMENT 'Executes a search on medical leaflets to retrieve the most relevant text documents based on the input query.'
# MAGIC RETURN SELECT
# MAGIC   content_chunked AS page_content,
# MAGIC   map('doc_uri', doc_uri, 'chunk_id', chunk_id) AS metadata
# MAGIC FROM
# MAGIC   vector_search(
# MAGIC     -- Specify your Vector Search index name here
# MAGIC     index => "${INDEX_NAME}",
# MAGIC     query => query,
# MAGIC     num_results => 1
# MAGIC   );

# COMMAND ----------
