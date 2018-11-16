import pandas

class simple_regression(object):
    def __init__(self):
        pass

    @staticmethod
    def train(df_input):
        """
        :param df_input: A pandas dataframe
        :return:
        """

        try:
            # add your code here
            
            #l contains number of columns
            l = len(df_input.columns)


            statistics_header = []
            for i in range(0,l):        
            statistics_header.append(df.columns[i])
        
            statistics_index = []
            statistics_index.append("Mean")
            statistics_index.append("Variance") 
            statistics_index.append("Standard Deviation")
            statistics_index.append("Co-variance") 
            statistics_index.append("Correlation Factor") 
            statistics_index.append("Is r significant?") 
            statistics_index.append("Partial Correlation Factor")



            coeff = {"m": 0.12, "c": 1.2} # this is testdata, replace with actual calculated data
            result = dict()
            result["coeff"] = coeff
            result["status"] = "success"
            return result
        
        except Exception as e:
            result = dict()
            result["coeff"] = {"error": str(e)}
            result["status"] = "failed"
            return result

    @staticmethod
    def score(df_input, dct_model):
        """
        :param df_input: A pandas Dataframe
        :param dct_model: A json model
        :return: df_output: A pandas dataframe
        """
        try:

            # add your code here







            df_output = pandas.DataFrame({"a": [1,2,3], "b":[2,3,4]}) # this is testdata, replace with actual calculated data
            result = "success"
            error = None
            return result, df_output, error
        except Exception as e:

            result = "failed"
            df_output = pandas.DataFrame() # send empty DF in case of failure
            error = str(e)
            return result, df_output, error
