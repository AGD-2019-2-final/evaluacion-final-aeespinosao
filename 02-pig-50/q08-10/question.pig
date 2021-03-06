-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
-- columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
-- registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
-- columna 3 es:
-- 
--   ((b,jjj), 216)
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data= LOAD 'data.tsv' AS (upper_letter:CHARARRAY, lower_letter: BAG{tup: TUPLE(letter:CHARARRAY)}, exam:MAP[]);
data = FOREACH data GENERATE FLATTEN(lower_letter) as lower, FLATTEN(exam) as exam;
data = GROUP data BY (lower,exam);
data = FOREACH data GENERATE group , COUNT($1);
STORE data INTO 'output';