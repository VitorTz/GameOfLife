#pragma once
#include "constants.h"


namespace gl {	

	class GameOfLife {
	
	private:
		bool* current_grid{};
		bool* next_grid{};		
		bool is_running{};

	private:
		int count_neighbors(int n);

	public:
		GameOfLife();
		~GameOfLife();
		void start();
		void pause();
		void reset();
		void random_grid();
		void update();
		void draw();

	};

}