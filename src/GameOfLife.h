#pragma once
#include "constants.h"
#include <filesystem>
#include <algorithm>
#include <cstdlib>
#include <string>


namespace gl {	

	class GameOfLife {
	
	private:
		bool* gen{};
		bool* next_gen{};
		bool* current_gen{};
		bool is_running{};
		int rows{ gl::GRID_ROWS };
		int cols{ gl::GRID_COLS };
		int grid_size{ gl::GRID_SIZE };
		int cell_size{ gl::CELL_SIZE };

	private:
		int count_neighbors(int n);

	public:
		GameOfLife();
		~GameOfLife();
		void change_cell_size(int delta);
		void start();
		void pause();
		void reset();
		void random_grid();
		void print();
		void update();
		void draw();

	};

}