from concurrent import futures
import calculator_pb2
import grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Calculator(calculator_pb2.CalculatorServicer):

  def Add(self, request, context):
    print("\nExecuting addition of {} and {} from server ".format(
          request.num1, request.num2))
    return calculator_pb2.AddReply(sum=request.num1+request.num2)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  calculator_pb2.add_CalculatorServicer_to_server(Calculator(), server)
  server.add_insecure_port('[::]:50050')
  print("Starting server...")
  server.start()
  print("Server is now started...")
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
