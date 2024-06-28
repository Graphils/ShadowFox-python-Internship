# Define the base class MobilePhone
class MobilePhone:
   def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram,storage):
     self.screen_type = screen_type
     self.network_type = network_type
     self.dual_im = dual_sim
     self.front_camera = front_camera
     self.Rear_camera_camera = rear_camera
     self.ram = ram
     self.storage = storage

# Define the child class Apple
class Apple(MobilePhone):
   def __init__(self, model, screen_type, network_type, dual_sim, front_camera,rear_camera, ram, storage):
     super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
     self.Model = model

# Define the child class Samsung
class Samsung(MobilePhone):
   def __init__(self, model, screen_type, network_type, dual_sim, front_camera,rear_camera, ram, storage):
     super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera,ram, storage)
     self.model = model

# Create an Apple iPhone
iphone = Apple('iPhone 13', 'Touch Screen', '5G', True, '12MP', '48MP', '4GB', '64GB')
print('Apple iphone Details:')
print('Model:', iphone.Model)
print('Screen Type:', iphone.screen_type)
print('Network Type:', iphone.network_type)

# Create a Samsung Galaxy
Galaxy = Samsung('Galaxy S22', 'Touch Screen', '5G', True, '16MP', '50MP', '4GB','128GB')
print("\nSamsug Galaxy Deatails:")
print("Model:", Galaxy.model)
print('screen type:',Galaxy.network_type)
