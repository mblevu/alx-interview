#!/usr/bin/python3
import pytest

island_perimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter:

    # returns 0 when given an empty grid
    def test_returns_0_when_given_an_empty_grid(self):
        # Arrange
        grid = []
    
        # Act
        result = island_perimeter(grid)
    
        # Assert
        assert result == 0

    # returns 4 when given a grid with a single cell with value 1
    def test_returns_4_when_given_a_grid_with_a_single_cell_with_value_1(self):
        # Arrange
        grid = [[1]]
    
        # Act
        result = island_perimeter(grid)
    
        # Assert
        assert result == 4

    # returns 10 when given a grid with a single row or column with all cells having value 1
    def test_returns_8_when_given_a_grid_with_a_single_row_or_column_with_all_cells_having_value_1(self):
        # Arrange
        grid = [[1, 1, 1, 1]]
    
        # Act
        result = island_perimeter(grid)
    
        # Assert
        assert result == 10

    # returns 0 when given a grid with all cells having value 0
    def test_returns_0_when_given_a_grid_with_all_cells_having_value_0(self):
        # Arrange
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
        # Act
        result = island_perimeter(grid)
    
        # Assert
        assert result == 0

    # returns 4 when given a grid with a single cell with value 1 and surrounded by cells with value 0
    def test_returns_4_when_given_a_grid_with_a_single_cell_with_value_1_and_surrounded_by_cells_with_value_0(self):
        # Arrange
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    
        # Act
        result = island_perimeter(grid)
    
        # Assert
        assert result == 4