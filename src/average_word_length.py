from pyspark import SparkContext, SparkConf


def calculate_average_word_length(input_file):
    # Create a Spark context
    conf = SparkConf().setAppName("AverageWordLength")
    sc = SparkContext(conf=conf)

    try:
        # Load the input text file
        lines = sc.textFile(input_file)

        # Calculate total word count and total word length
        word_lengths = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: len(word))

        total_word_count = word_lengths.count()
        total_word_length = word_lengths.sum()

        # Calculate the average word length
        average_word_length = total_word_length / total_word_count

        return average_word_length

    finally:
        # Stop the Spark context
        sc.stop()
