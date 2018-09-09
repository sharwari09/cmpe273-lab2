from __future__ import print_function
import calculator_pb2
import grpc

def run():
  channel = grpc.insecure_channel('localhost:50050')
  stub = calculator_pb2.CalculatorStub(channel)
  response = stub.Add(calculator_pb2.AddRequest(num1=50, num2=60))
  print("Addition of num1 and num2 is :\n")
  print(response.sum)

if __name__ == '__main__':
  run()
