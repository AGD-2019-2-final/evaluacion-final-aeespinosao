-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data= LOAD 'data.tsv' AS (upper_letter:CHARARRAY, lower_letter: BAG{tup: TUPLE(letter:CHARARRAY)}, exam:CHARARRAY);
data= FOREACH data GENERATE FLATTEN(lower_letter) AS letter;
result1= GROUP data BY letter;
result_count= FOREACH result1 GENERATE group, COUNT($1);
STORE result_count INTO 'output';

