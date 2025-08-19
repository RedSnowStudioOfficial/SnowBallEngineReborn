from SBTK_CORE import hash_table

class AnimationHashTable:
    def __init__(self):
        """
        Specialized hash table to store AnimationTK objects keyed by animation names.
        """
        self._hash_table = hash_table()
        self._current_animation_name = None

    def add_animation(self, name, animation):
        """
        Add or update an animation with the given name.
        :param name: str - animation name or ID
        :param animation: AnimationTK object
        """
        self._hash_table.put(name, animation)

    def get_animation(self, name):
        """
        Retrieve the AnimationTK object by name.
        :param name: str
        :return: AnimationTK or None if not found
        """
        return self._hash_table.get(name)

    def remove_animation(self, name):
        """
        Remove the animation by name.
        :param name: str
        :return: bool - True if removed, False if not found
        """
        if self._hash_table.remove(name):
            if self._current_animation_name == name:
                self._current_animation_name = None
            return True
        return False

    def switch_animation(self, name):
        """
        Switch the current animation to the one with the given name.
        :param name: str
        :return: bool - True if switched successfully, False if animation not found
        """
        if self._hash_table.contains_key(name):
            self._current_animation_name = name
            return True
        return False

    def get_current_animation(self):
        """
        Get the currently active AnimationTK object.
        :return: AnimationTK or None if no animation is active
        """
        if self._current_animation_name is None:
            return None
        return self._hash_table.get(self._current_animation_name)
