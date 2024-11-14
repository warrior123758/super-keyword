# basic one 
class parentclass:
    def parent_method(self):
        print("this is the parent method")
class childclass(parentclass):
    def child_method(self):
        print("this is the child method")
        super().parent_method() 
child_object=childclass()
child_object.child_method()


# to put both child_method and parent_method method under childclass
class parentclass:
    def parent_method(self):
        print("this is the parent method")
       
class childclass(parentclass):
    def parent_method(self):
        print("this is the 2nd time parent method")
        super().parent_method() 
    def child_method(self):
        print("this is the child method")
        super().parent_method() 

child_object=childclass()
child_object.child_method()
child_object.parent_method()
