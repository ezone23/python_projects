## pedometer
- pedometer program returning the running/walking status and counting the steps
- based on simple huristic algorithm
- results inferred from the sensor data changes

### status classification
- running/walking status denoted by status separator (0, 1, 2)
- status separator criteria
  - 0: still
  - 1: waling
  - 2: running
- each status defined by finding extremal values in the input data


### input and output
- program gets txt. file as an input
- input file contains acceleration sensor value that contains only the y-axis value(vertical to the ground)
- input values neglect the effect of graviational acceleration
- sensor delay: 20 ms
- program returns "output.txt" file as an output
- output file contains 'total step count', 'walking count', 'running count', and status separator for each index

#### included files
  - main file: pedometer.py
  - visualization program: vis_pedometer.py
  - sample test data: mixed.txt, run_sample.txt, sample1.txt, step_test1.txt
  - visualized image: running.png, standing.png, walking.png
