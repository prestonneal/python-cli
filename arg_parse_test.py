import fire
fire.Fire(lambda obj: type(obj).__name__)

# python example.py 10
# python example.py 10.0
# python example.py hello
# python example.py '(1,2)'
# python example.py [1,2]
# python example.py True
# python example.py {name:David}
# python example.py '{"name": "David Bieber"}'
# python example.py --obj=True
# python example.py --obj=False
# python example.py --obj
