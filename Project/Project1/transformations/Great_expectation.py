from pyspark import pipelines as dp


# Please edit the sample below


@dp.table
def great_expectation():
    return spark.read.table("samples.nyctaxi.trips")