-- Regenerates 7_Universe_Schema.json for the HarmonyGames universe.
-- Includes every declared service schema that exists in the DB, even ones with
-- zero tables -> emitted as {table_name: null, columns: []}.
-- Run in the universe Postgres DB; output is a single JSON array cell. Save the
-- contents of that cell -- not the one-row export wrapping it -- to 7_Universe_Schema.json.
WITH target_schemas(schema_name) AS (
  VALUES
    ('contacts'),('gcal'),('gdocs'),('gdrive'),('github'),
    ('gmail'),('gsheets'),('gslides'),('linear'),('slack'),('trello')
),
table_cols AS (
  SELECT
    c.table_schema,
    c.table_name,
    json_agg(
      json_build_object(
        'type',     c.data_type,
        'column',   c.column_name,
        'default',  c.column_default,
        'nullable', c.is_nullable,
        'position', c.ordinal_position
      ) ORDER BY c.ordinal_position
    ) AS cols
  FROM information_schema.columns c
  WHERE c.table_schema IN (SELECT schema_name FROM target_schemas)
     OR (c.table_schema = 'public' AND c.table_name = '_changelog')
  GROUP BY c.table_schema, c.table_name
),
all_rows AS (
  -- real tables (with their columns)
  SELECT table_schema, table_name, cols
  FROM table_cols

  UNION ALL

  -- declared schemas that exist in the DB but contain no tables
  SELECT s.schema_name, NULL::text AS table_name, NULL::json AS cols
  FROM target_schemas s
  JOIN information_schema.schemata sc ON sc.schema_name = s.schema_name
  WHERE NOT EXISTS (
    SELECT 1 FROM table_cols tc WHERE tc.table_schema = s.schema_name
  )
)
SELECT json_agg(
         json_build_object(
           'columns',      COALESCE(cols, '[]'::json),
           'table_name',   table_name,
           'table_schema', table_schema
         )
         ORDER BY table_schema, table_name NULLS FIRST
       ) AS universe_schema
FROM all_rows;
