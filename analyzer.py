import time
import matplotlib.pyplot as plt

class BigOAnalyzer:
    """
    A class to analyze and visualize the time complexity of functions.
    """

    @staticmethod
    def measure_runtime(func, input_generator, input_sizes):
        """
        Measures runtime for a given function across different input sizes.

        Args:
            func (callable): The function to analyze.
            input_generator (callable): A function to generate inputs based on size.
            input_sizes (list): List of input sizes to test.

        Returns:
            list: Runtimes corresponding to each input size.
        """
        runtimes = []
        for size in input_sizes:
            data = input_generator(size)
            start_time = time.time()
            func(data)
            end_time = time.time()
            runtimes.append(end_time - start_time)
        return runtimes

    @staticmethod
    def plot(input_sizes, runtimes, labels, title="Big-O Complexity Analysis"):
        """
        Plots runtimes against input sizes.

        Args:
            input_sizes (list): List of input sizes.
            runtimes (list): List of runtimes for each function.
            labels (list): Labels for the plotted lines.
            title (str): Title of the plot.
        """
        for runtime, label in zip(runtimes, labels):
            plt.plot(input_sizes, runtime, label=label)
        plt.xlabel("Input Size")
        plt.ylabel("Runtime (seconds)")
        plt.title(title)
        plt.legend()
        plt.show()
