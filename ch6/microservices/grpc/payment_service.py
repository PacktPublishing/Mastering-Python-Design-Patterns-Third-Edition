from concurrent import futures
import grpc
import payment_pb2
import payment_pb2_grpc


class PaymentServiceImpl(payment_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        # Process the payment (e.g., calling external APIs, database updates)
        # This is a simplified example. In reality, you'd have more complex logic.
        return payment_pb2.PaymentResponse(payment_id="12345", status="SUCCESS")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentServiceImpl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Payment Processing Service ready!")
    serve()
