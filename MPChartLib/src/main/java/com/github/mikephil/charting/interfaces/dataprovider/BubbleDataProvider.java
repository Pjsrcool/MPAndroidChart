package com.github.mikephil.charting.interfaces.dataprovider;

import com.github.mikephil.charting.data.BubbleData;

import javax.annotation.Nullable;

public interface BubbleDataProvider extends BarLineScatterCandleBubbleDataProvider {

    @Nullable
    BubbleData getBubbleData();
}
