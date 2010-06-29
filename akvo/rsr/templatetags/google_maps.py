# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from django import template
register = template.Library()

@register.inclusion_tag('inclusion_tags/_static_map.html')
def static_map(project, width, height, zoom, marker_color):
    base_url = 'http://maps.google.com/maps/api/staticmap?'
    query = 'markers=color:%s|%s&size=%sx%s&zoom=%d&sensor=false' % \
        (marker_color, project.get_location(), width, height, zoom)
    map_url = base_url + query
    return {'p': project,
            'map_url': map_url,
            'width': width,
            'height': height}

@register.inclusion_tag('inclusion_tags/_dynamic_map.html')
def dynamic_map(project, width, height, zoom, marker_color):
    return {'p': project,
            'width': width,
            'height': height,
            'zoom': zoom,
            'marker_color': marker_color}