CREATE DATABASE stockdb;

USE stockdb;

CREATE EXTERNAL TABLE stock_data (
  c double,
  h double,
  l double,
  o double,
  pc double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-bucket-name/raw-data/';
