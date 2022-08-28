import json
from definitions import ROOT_DIR


class Exercise:
    """class for exercise objects inside a workout"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.properties = self.get_properties(self.name)
        self.force = self.properties["force"]
        self.level = self.properties["level"]
        self.mechanic = self.properties["mechanic"]
        self.equipment = self.properties["equipment"]
        self.primary_muscles = self.properties["primaryMuscles"]
        self.secondary_muscles = self.properties["secondaryMuscles"]
        self.instructions = self.properties["instructions"]
        self.category = self.properties["category"]

    def get_properties(self, exercise_name: str) -> dict[str, str]:
        """Retrieves general properties of an exercise from json database"""
        database_path = (
            ROOT_DIR / "resources" / "exercise_database" / "exercises.json-master" / "exercises" / exercise_name
        )
        exercise_data_file = open(database_path / "exercise.json")
        exercise_database = json.load(exercise_data_file)
        exercise_data_file.close()
        return exercise_database


if __name__ == "__main__":
    test_object = Exercise(input("\nEnter name of exercise:\t"))
    test_object.get_properties(test_object.name)
    # print(test_object.properties)
    print(test_object.primary_muscles)
