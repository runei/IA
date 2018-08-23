#include <iostream>
#include <vector>
#include <random>

#define N 10

struct City
{
	int x;
	int y;

	City(int _x, int _y) : x(_x), y(_y) {};
};

int random(int min, int max)
{
	std::random_device rd;
	std::default_random_engine e1(rd());
	std::uniform_int_distribution<int> ud(min, max);
	return ud(e1);
}

double random_d(int min, int max)
{
	std::random_device rd;
	std::default_random_engine e1(rd());
	std::uniform_real_distribution<double> ud(min, max);
	return ud(e1);
}

std::vector<City> createCities()
{
	std::vector<City> cities;

	for (int i = 0; i < N; ++i)
	{
		cities.push_back(City(random(0, 200), random(0, 200)));
	}
	return cities;
}

double distance(City c1, City c2)
{
	int x = std::abs(c1.x - c2.x);
	int y = std::abs(c1.y - c2.y);
	return std::sqrt( x*x + y*y );
}

double totalDistance(std::vector<City> cities)
{
	double result;
	for (int i = 1; i < cities.size(); ++i)
	{
		result += distance(cities[i - 1], cities[i]);
	}
	return result;
}

double probability(int energy, int new_energy, double temperature)
{
	if (new_energy < energy) return 1.0;
	return std::exp((energy - new_energy) / temperature);
}

int main()
{
	auto cities = createCities();

	double temp = 10000;
	double rate = 0.003;

	std::cout << totalDistance(cities) << "\n";
	auto best(cities);

	while (temp > 1)
	{
		auto new_result(cities);
		int pos1 = random(0, (int) cities.size());
		int pos2 = random(0, (int) cities.size());

		new_result[pos1] = cities[pos2];
		new_result[pos2] = cities[pos1];

		for (auto city : new_result)
		{
			std::cout << city.x << "\t" << city.y << "\n";
		}
break;
		int current_energy = totalDistance(cities);
		int new_energy = totalDistance(new_result);

		if (probability(current_energy, new_energy, temp) > random_d(0, 1))
		{
			cities.swap(new_result);
		}		

		if (totalDistance(cities) < totalDistance(best))
		{
			best.swap(cities);
			std::cout << totalDistance(best) << "\n";
		}

		temp *= 1 - rate;
	}

	return 0;
}