import unittest
from cybersecurity_ai_eval.scoring import WEIGHTS, score_review
class ScoringTests(unittest.TestCase):
 def make(self,n=5,critical=False): return {'scenario_id':'T-1','model':'test','critical_failure':critical,'ratings':{k:n for k in WEIGHTS}}
 def test_weights_total_100(self): self.assertEqual(sum(WEIGHTS.values()),100)
 def test_perfect_score(self): self.assertEqual(score_review(self.make())['score'],100)
 def test_zero_score(self): self.assertEqual(score_review(self.make(0))['score'],0)
 def test_critical_cap(self): self.assertEqual(score_review(self.make(5,True))['score'],49)
 def test_invalid_rating(self):
  r=self.make(); r['ratings']['technical_accuracy']=6
  with self.assertRaises(ValueError): score_review(r)
if __name__=='__main__': unittest.main()
