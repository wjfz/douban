# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb import request_pb2 as pb_dot_request__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetBookInfo = channel.unary_unary(
        '/pb.Greeter/GetBookInfo',
        request_serializer=pb_dot_request__pb2.GetBookInfoReq.SerializeToString,
        response_deserializer=pb_dot_request__pb2.GetBookInfoResp.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetBookInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetBookInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetBookInfo,
          request_deserializer=pb_dot_request__pb2.GetBookInfoReq.FromString,
          response_serializer=pb_dot_request__pb2.GetBookInfoResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))