# Example usage:
from h2gis import H2gisConnector
import time
import statistics


h2gis = H2gisConnector("./h2gis/h2gis.so")
h2gis.connect("./test", "sa", "sa")


#currently the two linew below are not working, you must do it via the .jar of h2gis, otherwise nothing will work
h2gis.execute_update("CREATE ALIAS IF NOT EXISTS H2GIS_SPATIAL FOR \"org.h2gis.functions.factory.H2GISFunctions.load\";")

h2gis.execute_update("DROP TABLE TEST IF EXISTS;")


times_nat = []
i = 0
for i in range(0, 50):
    start = time.perf_counter()
    h2gis.execute_update("DROP TABLE TEST IF EXISTS;")
    h2gis.execute_update("CALL GeoJsonRead('./test.geojson');")
    end = time.perf_counter()
    times_nat.append(end - start)
    print("etape ", i, "finished")

print("elapsed native time ", sum(times_nat))

print("average native time ", statistics.mean(times_nat))

h2gis.close()