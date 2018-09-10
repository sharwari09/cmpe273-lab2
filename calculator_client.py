from __future__ import print_function
import calculator_pb2
import grpc

def run():
  num1 = 300
  num2 = 900
  channel = grpc.insecure_channel('localhost:50050')
  stub = calculator_pb2.CalculatorStub(channel)
  response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
  print("Addition of {} and {} is :: {}".format(num1, num2, response.sum))

if __name__ == '__main__':
  run()
