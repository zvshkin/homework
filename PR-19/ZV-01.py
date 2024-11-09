import sandwich
sandwich.make_sandwich("сыр", "помидоры", "ветчина")

from sandwich import make_sandwich
make_sandwich("бекон", "салат", "помидоры")

from sandwich import make_sandwich as ZV
ZV("курица", "сыр", "перец")

import sandwich as mq
mq.make_sandwich("рыба", "помидоры")

from sandwich import *
make_sandwich("оливки", "огурец")