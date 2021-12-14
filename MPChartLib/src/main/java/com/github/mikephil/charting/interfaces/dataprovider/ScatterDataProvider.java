package com.github.mikephil.charting.interfaces.dataprovider;

import com.github.mikephil.charting.data.ScatterData;

import javax.annotation.Nullable;

public interface ScatterDataProvider extends BarLineScatterCandleBubbleDataProvider {

    @Nullable
    ScatterData getScatterData();
}
