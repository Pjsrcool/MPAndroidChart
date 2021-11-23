package com.github.mikephil.charting.interfaces.dataprovider;

import com.github.mikephil.charting.data.CandleData;

import javax.annotation.Nullable;

public interface CandleDataProvider extends BarLineScatterCandleBubbleDataProvider {

    @Nullable
    CandleData getCandleData();
}
