from utils.Log import CamperException, CamperLogger

logger = CamperLogger(__name__, log_path='', debug=True)
@CamperException.catch
def example():
    1 / 0


example()
