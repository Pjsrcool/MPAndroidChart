package com.github.mikephil.charting.interfaces.dataprovider;

import com.github.mikephil.charting.data.CombinedData;
import androidx.annotation.Nullable;
/**
 * Created by philipp on 11/06/16.
 */

public interface CombinedDataProvider extends LineDataProvider, BarDataProvider, BubbleDataProvider, CandleDataProvider, ScatterDataProvider {

    CombinedData getCombinedData();
}
