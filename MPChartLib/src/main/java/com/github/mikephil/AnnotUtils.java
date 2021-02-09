package com.github.mikephil;

import javax.annotation.Nonnull;

public class AnnotUtils {

  static @Nonnull <T> T downCast(T item) {
    if (item == null) {
      throw new RuntimeException("Shouldn't have been null");
    }
    return item;
  }
}
