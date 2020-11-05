import pkg_resources

import azimuth
import azimuth.model_comparison
import numpy as np
import unittest
import pandas
import os
dirname, filename = os.path.split(os.path.abspath(__file__))


class SavedModelTests(unittest.TestCase):
    """
    This unit test checks that the predictions for 1000 guides match the predictions we expected in Nov 2016.
    This unit test can fail due to randomness in the model (e.g. random seed, feature reordering).
    """

    def test_predictions_nopos(self):
        with pkg_resources.resource_stream('azimuth', os.path.join("tests", "1000guides.csv")) as f:
            df = pandas.read_csv(f, index_col=0)
        predictions = azimuth.model_comparison.predict(np.array(df['guide'].values), None, None)

        num = 0
        for i, (e, a) in enumerate(zip(predictions, df['truth nopos'])):
            if abs(e - a) > 1e-3:
                print("{}:".format(i), e, a)
                num += 1
        if num > 0:
            print("Num errors: ", num)

        self.assertTrue(np.allclose(predictions, df['truth nopos'].values, atol=1e-3))

    def test_predictions_pos(self):
        with pkg_resources.resource_stream('azimuth', os.path.join("tests", "1000guides.csv")) as f:
            df = pandas.read_csv(f, index_col=0)
        predictions = azimuth.model_comparison.predict(np.array(df['guide'].values), np.array(df['AA cut'].values), np.array(df['Percent peptide'].values))

        num = 0
        for i, (e, a) in enumerate(zip(predictions, df['truth pos'])):
            if abs(e - a) > 1e-3:
                print("{}:".format(i), e, a)
                num += 1
        if num > 0:
            print("Num errors: ", num)

        self.assertTrue(np.allclose(predictions, df['truth pos'].values, atol=1e-3))


        
if __name__ == '__main__':
    unittest.main()
