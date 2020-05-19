# MIT-6.00.1x-Problem-set-2

Those are my containerized programs solving the 2nd problem set of the course "Introduction to Computer Science and Programming Using Python" (MIT 6.00.1x) of the Massachusetts Institute of Technology.

You can find the all the instructions for that problem set on edx.org.

Problem 1:
That program calculates the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

Problem 2:
That program calculates the minimum fixed monthly payment (constant amount that will be paid each month) needed in order pay off a credit card balance within 12 months. 

Problem 3:
That program serves the same purpose as the program 2 but it uses bisection search in order to be executed faster.

For each problem solution, open the corresponding problem repository in your UNIX terminal and run the following command:
sudo docker build -t mit-python-problem-2 . && echo -e "\n\n" && sudo docker run -i -t mit-python-problem-2
