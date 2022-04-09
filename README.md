# augan-forkgan-bdd-dataset

Dataset is BDD100K.
With 2 scripts, I managed to make train/test folders, for AU-GAN (and / or ForkGAN).

https://github.com/jgkwak95/AU-GAN

https://github.com/zhengziqiang/ForkGAN

"We reorganized this dataset for night-to-day and day-to-night tasks according to the daytime annotation, and obtained 27,971/3,929 train/val split for night images and 36,728/5,258 train/test split for day images."

```
# The directory structure of flower should be this:
├── bdd100k
  ├── trainA (rainy night - 27971 images)
      ├── images here...
  ├── trainB (daytime - 36728 images)
      ├── images here...
  ├── testA (rainy night - 3929 images)
      ├── images here...
  ├── testb (daytime - 5258 images)
      ├── images here...
```

https://bdd-data.berkeley.edu/portal.html#download

(As I understand) license allows to put it here.

Permission to use, copy, modify, and **distribute** this software and its documentation for educational, research, and not-for-profit purposes, without fee and without a signed licensing agreement; and permission to use, copy, modify and distribute this software for commercial purposes (such rights not subject to transfer) to BDD and BAIR Commons members and their affiliates, **is hereby granted**

But if I am wrong and if anyone from BDD100K dataset has an issue with that, please just write here, will delete it immediately.


### Using in Google Colab
```
!git clone https://github.com/ptrxpl/augan-forkgan-bdd-dataset.git

import os

dir = "augan-forkgan-bdd-dataset/bdd100k/"

list_trainA = os.listdir(dir + "trainA")
list_trainB = os.listdir(dir + "trainB")
list_testA = os.listdir(dir + "testA")
list_testB = os.listdir(dir + "testB")

print("trainA: " + str(len(list_trainA)))
print("trainB: " + str(len(list_trainB)))
print("testA: " + str(len(list_testA)))
print("testB: " + str(len(list_testB)))

# Should be:
# trainA: 27971
# trainB: 36728
# testA: 3929
# testB: 5258
```
