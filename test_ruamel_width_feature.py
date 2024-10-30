import ruamel.yaml
import unittest

class TestYAMLWidth(unittest.TestCase):
    def setUp(self):
        # Create a YAML instance with the desired configuration
        self.yaml = ruamel.yaml.YAML()
        self.yaml.width = 80

        # Load input.yaml
        with open('input.yaml', 'r') as infile:
            self.input_data = self.yaml.load(infile)

        # Generate output.yaml
        with open('output.yaml', 'w') as outfile:
            self.yaml.dump(self.input_data, outfile)


    def test_line_width(self):
        # Check each line in the generated output.yaml
        with open('output.yaml', 'r') as outfile:
            for line in outfile:
                line_length = len(line.rstrip())
                self.assertLessEqual(line_length, 80,
                                     f"Line exceeds 80 characters: {line.rstrip()} (Length: {line_length})")

        # Test output:
        # AssertionError: 84 not less than or equal to 80 : Line exceeds 80 characters:         key: this is a quite long string that should be reformatted to use less than (Length: 84)

if __name__ == '__main__':
    unittest.main()