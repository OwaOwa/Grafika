from pyglet.gl import *

class Triangle :
	def __init__(self):
		self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-0.5,-0.5,0.0,0.5,-0.5,0.0,0.0,0.5,0.0]),
														('c3b', [100,200,220,200,110,100,100,250,100]))

class MyWindow (pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super(MyWindow,self).__init__(*args, **kwargs)
		self.set_minimum_size(400, 300)													

		self.triangle = Triangle()

	def on_draw(self) :
		self.triangle.vertices.draw(GL_TRIANGLES)

	def on_resize(self,width, height):
		glViewport(0,0,width,height)


if __name__ == "__main__":
	window = MyWindow(1280,720, "Cek", resizable=True)
	pyglet.app.run()