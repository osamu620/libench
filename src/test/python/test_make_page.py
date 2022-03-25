import unittest
import os
import make_page


class MakePageTest(unittest.TestCase):

  BUILD_DIR = "build/python_test"
  BIN_PATH = "./build/libench"

  def setUp(self):
    os.makedirs(MakePageTest.BUILD_DIR, exist_ok=True)

  def test_make(self):
    images = (
      make_page.Image(
        name = "Sample PNG RGBA image",
        size=64000,
        preview_path="src/test/resources/rgba.png",
        src_path="src/test/resources/rgba.png",
        codecs = (
          make_page.Codec(name="HT", coded_size=12000, encode_time=0.5, decode_time=0.5),
          make_page.Codec(name="J2K1", coded_size=10000, encode_time=0.1, decode_time=0.1),
          make_page.Codec(name="PNG", coded_size=14000, encode_time=0.3, decode_time=0.3)
        )
      ),
      make_page.Image(
        name="Sample TIFF image",
        size=20000000,
        preview_path="src/test/resources/rgba.png",
        src_path="src/test/resources/rgba.png",
        codecs = (
          make_page.Codec(name="HT", coded_size=10000000, encode_time=0.8, decode_time=0.9),
          make_page.Codec(name="J2K1", coded_size=9000000, encode_time=0.12, decode_time=0.12),
          make_page.Codec(name="PNG", coded_size=13000000, encode_time=0.2, decode_time=0.3)
        )
      )
    )

    make_page.build(MakePageTest.BUILD_DIR, images)

  def run_perf_tests(self):
    results = make_page.run_perf_tests("src/test/resources", MakePageTest.BIN_PATH)

    self.assertIsNotNone(results)
    self.assertEqual(len(results), 8)

  def test_make_analysis(self):
    make_page.make_analysis("src/test/resources/results.csv", "build/figure.png")
