import grpc
import payment_pb2
import payment_pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = payment_pb2_grpc.PaymentServiceStub(channel)
        response = stub.ProcessPayment(
            payment_pb2.PaymentRequest(
                order_id="order123", amount=99.99, currency="USD", user_id="user456"
            )
        )
        print("Payment service responded with status: " + response.status)


if __name__ == "__main__":
    main()
