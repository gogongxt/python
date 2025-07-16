import torch

from typing import List


def custom_backend(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
    print("custom backend called with FX graph:")
    gm.graph.print_tabular()
    print("\n\n")
    return gm.forward


# Reset since we are using a different backend.
torch._dynamo.reset()


def bar(a, b):
    x = a / (torch.abs(a) + 1)
    if b.sum() < 0:
        b = b * -1
    return x * b


opt_bar = torch.compile(bar, backend=custom_backend)
inp1 = torch.randn(10)
inp2 = torch.randn(10)
opt_bar(inp1, inp2)
opt_bar(inp1, -inp2)


"""
custom backend called with FX graph:
opcode         name    target                                                  args         kwargs
-------------  ------  ------------------------------------------------------  -----------  --------
placeholder    l_a_    L_a_                                                    ()           {}
placeholder    l_b_    L_b_                                                    ()           {}
call_function  abs_1   <built-in method abs of type object at 0x7fdcc3cf6fa0>  (l_a_,)      {}
call_function  add     <built-in function add>                                 (abs_1, 1)   {}
call_function  x       <built-in function truediv>                             (l_a_, add)  {}
call_method    sum_1   sum                                                     (l_b_,)      {}
call_function  lt      <built-in function lt>                                  (sum_1, 0)   {}
output         output  output                                                  ((x, lt),)   {}



custom backend called with FX graph:
opcode         name    target                   args         kwargs
-------------  ------  -----------------------  -----------  --------
placeholder    l_b_    L_b_                     ()           {}
placeholder    l_x_    L_x_                     ()           {}
call_function  b       <built-in function mul>  (l_b_, -1)   {}
call_function  mul_1   <built-in function mul>  (l_x_, b)    {}
output         output  output                   ((mul_1,),)  {}



custom backend called with FX graph:
opcode         name    target                   args          kwargs
-------------  ------  -----------------------  ------------  --------
placeholder    l_x_    L_x_                     ()            {}
placeholder    l_b_    L_b_                     ()            {}
call_function  mul     <built-in function mul>  (l_x_, l_b_)  {}
output         output  output                   ((mul,),)     {}
"""


# Reset since we are using a different backend.
torch._dynamo.reset()
explain_output = torch._dynamo.explain(bar)(torch.randn(10), torch.randn(10))
print(explain_output)


"""
Graph Count: 2
Graph Break Count: 1
Op Count: 6
Break Reasons:
  Break Reason 1:
    Reason: generic_jump TensorVariable()
    User Stack:
      <FrameSummary file /nfs/ofs-llm-ssd/user/gogongxt/Projects/python/torch_compile/03_custom_backend.py, line 19 in bar>
Ops per Graph:
  Ops 1:
    <built-in method abs of type object at 0x7f8a5eaf6fa0>
    <built-in function add>
    <built-in function truediv>
    <built-in function lt>
  Ops 2:
    <built-in function mul>
    <built-in function mul>
Out Guards:
  Guard 1:
    Name: ''
    Source: global
    Create Function: DEFAULT_DEVICE
    Guard Types: ['DEFAULT_DEVICE']
    Code List: ['utils_device.CURRENT_DEVICE == None']
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 2:
    Name: ''
    Source: global
    Create Function: GRAD_MODE
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 3:
    Name: ''
    Source: shape_env
    Create Function: SHAPE_ENV
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 4:
    Name: "L['a']"
    Source: local
    Create Function: TENSOR_MATCH
    Guard Types: ['TENSOR_MATCH']
    Code List: ["hasattr(L['a'], '_dynamo_dynamic_indices') == False"]
    Object Weakref: <weakref at 0x7f8774331b20; dead>
    Guarded Class Weakref: <weakref at 0x7f8996173240; to 'torch._C._TensorMeta' at 0x5850e30 (Tensor)>
  Guard 5:
    Name: "L['b'].sum"
    Source: local
    Create Function: HASATTR
    Guard Types: ['HASATTR']
    Code List: ["hasattr(L['b'], 'sum')"]
    Object Weakref: <weakref at 0x7f87743304a0; dead>
    Guarded Class Weakref: <weakref at 0x7f8996173240; to 'torch._C._TensorMeta' at 0x5850e30 (Tensor)>
  Guard 6:
    Name: ''
    Source: global
    Create Function: DETERMINISTIC_ALGORITHMS
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 7:
    Name: "L['b']"
    Source: local
    Create Function: TENSOR_MATCH
    Guard Types: ['TENSOR_MATCH']
    Code List: ["hasattr(L['b'], '_dynamo_dynamic_indices') == False"]
    Object Weakref: <weakref at 0x7f87743304a0; dead>
    Guarded Class Weakref: <weakref at 0x7f8996173240; to 'torch._C._TensorMeta' at 0x5850e30 (Tensor)>
  Guard 8:
    Name: ''
    Source: global
    Create Function: TORCH_FUNCTION_STATE
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 9:
    Name: "G['torch']"
    Source: global
    Create Function: FUNCTION_MATCH
    Guard Types: ['ID_MATCH']
    Code List: ["___check_obj_id(G['torch'], 140232406321328)"]
    Object Weakref: <weakref at 0x7f8774332930; to 'module' at 0x7f8a66c3c8b0>
    Guarded Class Weakref: <weakref at 0x7f8a67557010; to 'type' at 0x936c60 (module)>
  Guard 10:
    Name: "G['torch'].abs"
    Source: global
    Create Function: FUNCTION_MATCH
    Guard Types: ['ID_MATCH']
    Code List: ["___check_obj_id(G['torch'].abs, 140232401646624)"]
    Object Weakref: <weakref at 0x7f8774333b00; to 'builtin_function_or_method' at 0x7f8a667c7420>
    Guarded Class Weakref: <weakref at 0x7f8a675244a0; to 'type' at 0x9371a0 (builtin_function_or_method)>
  Guard 11:
    Name: ''
    Source: global
    Create Function: DEFAULT_DEVICE
    Guard Types: ['DEFAULT_DEVICE']
    Code List: ['utils_device.CURRENT_DEVICE == None']
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 12:
    Name: ''
    Source: global
    Create Function: GRAD_MODE
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 13:
    Name: "L['b']"
    Source: local
    Create Function: TENSOR_MATCH
    Guard Types: ['TENSOR_MATCH']
    Code List: ["hasattr(L['b'], '_dynamo_dynamic_indices') == False"]
    Object Weakref: <weakref at 0x7f87743304a0; dead>
    Guarded Class Weakref: <weakref at 0x7f8996173240; to 'torch._C._TensorMeta' at 0x5850e30 (Tensor)>
  Guard 14:
    Name: ''
    Source: shape_env
    Create Function: SHAPE_ENV
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 15:
    Name: ''
    Source: global
    Create Function: DETERMINISTIC_ALGORITHMS
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
  Guard 16:
    Name: "L['x']"
    Source: local
    Create Function: TENSOR_MATCH
    Guard Types: ['TENSOR_MATCH']
    Code List: ["hasattr(L['x'], '_dynamo_dynamic_indices') == False"]
    Object Weakref: <weakref at 0x7f8773115800; dead>
    Guarded Class Weakref: <weakref at 0x7f8996173240; to 'torch._C._TensorMeta' at 0x5850e30 (Tensor)>
  Guard 17:
    Name: ''
    Source: global
    Create Function: TORCH_FUNCTION_STATE
    Guard Types: None
    Code List: None
    Object Weakref: None
    Guarded Class Weakref: None
Compile Times: TorchDynamo compilation metrics:
Function                        Runtimes (s)
------------------------------  --------------
_compile.compile_inner          0.0129, 0.0075
OutputGraph.call_user_compiler  0.0001, 0.0001
gc                              0.0003, 0.0002
"""
