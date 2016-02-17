
import funtool.state_measure
import numbers

@funtool.state_measure.state_and_parameter_measure
def least_ray( state, parameters):
    try:
        ray_mag= min([ ray.magnitude for ray in state.data.get('full_rays')  ])
    except:
        ray_mag= None
    return ray_mag

def _least_ray( state, parameters):
    try:
        ray_mag= min([ ray.magnitude for ray in state.data.get('full_rays')  ])
    except:
        ray_mag= None
    return ray_mag
