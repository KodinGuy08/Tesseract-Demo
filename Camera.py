import cv2, queue, threading, time

# bufferless VideoCapture
class VideoCapture:

  def __init__(self, name, callback=None):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()

    self.callback = callback
    self.callbackEnabled = False
    
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()

      if self.callback is not None and self.callbackEnabled:
        self.callback(frame)
      
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

  def pause(self):
    self.callbackEnabled = False
    
  def start(self):
    self.callbackEnabled = True
