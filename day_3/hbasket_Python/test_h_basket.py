import unittest
from domain_factory import DomainFactory

from unittest.mock import patch, MagicMock
from h_basket import HamaraBasket
class TestHamaraBasket(unittest.TestCase):
    def setUp(self):
        self.domain_factory = DomainFactory()

    def test_should_reduce_sell_in_by_one(self):
        # Arrange
        name = "Regular Item"
        sell_in = 10
        quality = 10
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, sell_in - 1)

    def test_should_reduce_quality_by_one(self):
        # Arrange
        name = "Regular Item"
        sell_in = 10
        quality = 10
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].quality, quality - 1)

    def test_quality_decreases_twice_as_fast_after_sell_in(self):
        # Arrange
        name = "Regular Item"
        sell_in = 0
        quality = 10
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, -1)

    def test_quality_decreases_twice_as_fast_after_quality(self):
        # Arrange
        name = "Regular Item"
        sell_in = 0
        quality = 10    
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].quality, 8)

    def test_quality_never_goes_below_zero(self):
        # Arrange
        name = "Regular Item"
        sell_in = 5
        quality = 0
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 0)

    def test_indian_wine_increases_in_quality(self):
        # Arrange
        name = "Indian Wine"
        sell_in = 10
        quality = 20
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 21)

    def test_indian_wine_quality_never_exceeds_50(self):
        # Arrange
        name = "Indian Wine"
        sell_in = 10
        quality = 50
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)
        
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 50)

    def test_forest_honey_does_not_change(self):
        # Arrange
        name = "Forest Honey"
        sell_in = 10
        quality = 30
        items = self.domain_factory.single_item_provider(name, sell_in, quality)
        
        # Act
        self.domain_factory.update_quality(items)
        print(items[0].sell_in)
        print(items[0].quality)
        # Assert
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 30)

    def test_movie_tickets_increase_by_2_when_10_days_or_less(self):
        # Arrange
        name = "Movie Tickets"
        sell_in = 10
        quality = 20
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 22)

    def test_movie_tickets_increase_by_3_when_5_days_or_less(self):
        # Arrange
        name = "Movie Tickets"
        sell_in = 5
        quality = 20
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 23)

    def test_movie_tickets_quality_drops_to_zero_after_concert(self):
        # Arrange
        name = "Movie Tickets"
        sell_in = 0
        quality = 20
        items = self.domain_factory.single_item_provider(name, sell_in, quality)

        # Act
        self.domain_factory.update_quality(items)

        # Assert
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)
    @patch.object(HamaraBasket, 'update_quality')
    def test_for_quality_update_call(self, mock_update_quality):
        name = "Forest Honey"
        sell_in = 10
        quality = 30
        items = self.domain_factory.single_item_provider(name, sell_in, quality)
        
        # Act
        # self.domain_factory.update_quality(items)
        # print(items[0].sell_in)
        # print(items[0].quality)


        self.domain_factory.update_quality(items)

        # Assert
        mock_update_quality.assert_called_once()
        

if __name__ == "__main__":
    unittest.main()
