class Specification:

    _map = {
        'base': ['none', 'anticlockwise', 'clockwise'],
        'shoulder': ['none', 'up', 'down'],
        'elbow': ['none', 'up', 'down'],
        'wrist': ['none', 'up', 'down'],
        'grip': ['none', 'open', 'close'],
        'light': ['on', 'off'],
    }

    _defaults = {
        'base': 'none',
        'shoulder': 'none',
        'elbow': 'none',
        'wrist': 'none',
        'grip': 'none',
        'light': 'off',
    }

    _valid_components = frozenset(['base', 'shoulder', 'elbow', 'wrist', 'grip', 'light'])

    _specification = {}

    def __init__(self, specification):
        Specification.__validate_spec(specification)

        self._specification = Specification.__create_full_specification(Specification._defaults, specification)

    def __create_full_specification(defaults, specification):
        full_specification = {}
        
        for component, default_setting in defaults.items():
            full_specification[component] = specification[component] if component in specification else default_setting

        return full_specification

    def __validate_spec(specification):
        invalid_components = frozenset(specification.keys()).difference(Specification._valid_components)

        if len(invalid_components) > 1:
            raise UnrecognisedComponentException(invalid_components)

        for component, setting in specification.items():
            Specification.__validate_component_setting(component, setting)

        return True

    def __validate_component_setting(component, setting):
        if (setting not in Specification._map[component]):
            raise InvalidComponentSettingException(component, setting)

        return True

    def get_all_settings(self):
        return self._specification

    def get_settings_for_component(self, component):
        if (component not in self._specification):
            raise UnrecognisedComponentException([component])

        return self._specification[component]

    def union(self, specification):
        return Specification(Specification.__create_full_specification(self._specification, specification))



class SpecificationException(Exception):
    pass



class UnrecognisedComponentException(SpecificationException):
    _invalid_components = None

    def __init__(self, invalid_components):
        super(UnrecognisedComponentException, self).__init__('Unrecognised component(s): %s' % ','.join(invalid_components))
        self._invalid_components = invalid_components

    def get_invalid_components(self):
        return self._invalid_components



class InvalidComponentSettingException(SpecificationException):
    _component_name = None
    _invalid_setting = None
    
    def __init__(self, component_name, invalid_setting):
        super(InvalidComponentSettingException, self).__init__('Unrecognised setting \'%s\' for component: %s' % (invalid_setting, component_name))
        self._component_name = component_name
        self._invalid_setting = invalid_setting

    def get_component_name(self):
        return self._component_name
    
    def get_invalid_setting(self):
        return self._invalid_setting
