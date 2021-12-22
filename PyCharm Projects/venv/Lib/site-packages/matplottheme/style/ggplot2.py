'''
ggplot2 Style
=============

'''
from .default import Style


class ggplot2Style(Style):

    '''
    This class is a collection of all painting methods provided by the 
    ggplot2 style of MatPlotTheme.

    :param palette: The palette used for coloring.
    '''

    def legend(self, ax, *args, **kwargs):
        '''
        Place a legend to the input :class:`matplotlib.axes.Axes` object.

        :param ax: The input axes object.
        :param position: The position of the legend. Default is ``'right'``. Value
                can be ``'left'``, ``'right'``, ``'top'``, or ``'bottom'``.
        :param fraction: The fraction of the height/width of the axes 
                object that will be shrunk to fit the legend.
        :return: The legend

        All additional input parameters are passed to :meth:`~matplotlib.axes.legend`.

        .. note::
           The legend in ggplot2 may not work well with ``fig.tight_layout()``, 
           which resizes and repositions the :class:`matplotlib.axes.Axes` objects.

        .. seealso::
           :meth:`matplotlib.axes.legend` for documentation on valid kwargs.
        '''
        import matplotlib.transforms as mtrans

        fraction = kwargs.pop('fraction', 0.15)
        box = ax.get_position(original=True)

        position = kwargs.pop('position', 'right')
        if position == 'left':
            kwargs.setdefault('loc', 'center right')
            kwargs.setdefault('bbox_to_anchor', (-0.1, 0.5))
            _, _, ax_box = box.splitx(fraction, fraction + 0.1)
        elif position == 'right':
            kwargs.setdefault('loc', 'center left')
            kwargs.setdefault('bbox_to_anchor', (1, 0.5))
            ax_box, _, _ = box.splitx(
                0.95 - fraction, 1 - fraction)
        elif position == 'top':
            kwargs.setdefault('loc', 'lower center')
            kwargs.setdefault('bbox_to_anchor', (0.5, 1.0))
            kwargs.setdefault('ncol', 100)
            _, _, ax_box = box.splity(fraction, fraction + 0.05)
        elif position == 'bottom':
            kwargs.setdefault('loc', 'upper center')
            kwargs.setdefault('bbox_to_anchor', (0.5, -0.1))
            kwargs.setdefault('ncol', 100)
            ax_box, _, _ = box.splity(
                0.85 - fraction, 1 - fraction)
        else:
            raise ValueError("{value} is not a valid position."
                             .format(value=position))

        transform = mtrans.BboxTransform(box, ax_box)
        pos = mtrans.Bbox(transform.transform(ax.get_position()))
        ax.set_position(pos)

        kwargs.setdefault('frameon', False)

        legend = ax.legend(*args, **kwargs)

        if not legend:
            raise ValueError("Legend is not generated. Do you add labels "
                             "to the source data?")

        texts = legend.texts
        for t in texts:
            t.set_color(self.palette.dark_frame)
        legend.get_title().set_color(self.palette.dark_frame)

        return legend

    def plot(self, ax, *args, **kwargs):
        '''
        Add a line plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.plot`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.plot` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.plot(self, ax, *args, **kwargs)

        self._post_process(ax)

        return result

    def bar(self, ax, position, length, width=0.8, offset=None, *args, **kwargs):
        '''
        Add a bar plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.bar`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'auto'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.bar` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'auto')

        result = Style.bar(
            self, ax, position, length, width, offset, *args, **kwargs)

        self._post_process(ax)

        return result

    def scatter(self, ax, x, y, *args, **kwargs):
        '''
        Add a scatter plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.scatter`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.scatter` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.scatter(self, ax, x, y, *args, **kwargs)

        self._post_process(ax)

        return result

    def hist(self, ax, x, *args, **kwargs):
        '''
        Add a histogram plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.hist`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'auto'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.hist` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'auto')

        result = Style.hist(self, ax, x, *args, **kwargs)

        self._post_process(ax)

        return result

    def boxplot(self, ax, x, *args, **kwargs):
        '''
        Add a box plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.boxplot`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'auto'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.boxplot` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'auto')

        result = Style.boxplot(self, ax, x, *args, **kwargs)

        self._post_process(ax)

        return result

    def cohere(self, ax, x, y, *args, **kwargs):
        '''
        Add a coherence plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.cohere`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.cohere` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.cohere(self, ax, x, y, *args, **kwargs)

        self._post_process(ax)

        return result

    def csd(self, ax, x, y, *args, **kwargs):
        '''
        Add a cross-spectral density plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.csd`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.csd` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.csd(self, ax, x, y, *args, **kwargs)

        self._post_process(ax)

        return result

    def psd(self, ax, x, *args, **kwargs):
        '''
        Add a power spectral density plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.psd`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.psd` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.psd(self, ax, x, *args, **kwargs)

        self._post_process(ax)

        return result

    def errorbar(self, ax, x, y, *args, **kwargs):
        '''
        Add an errorbar plot to the input :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.errorbar`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.errorbar` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.errorbar(self, ax, x, y, *args, **kwargs)

        self._post_process(ax)

        return result

    def fill_between(self, ax, x, y1, *args, **kwargs):
        '''
        Add filled polygons to :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.fill_between`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.fill_between` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.fill_between(self, ax, x, y1, *args, **kwargs)

        self._post_process(ax)

        return result

    def fill_betweenx(self, ax, y, x1, *args, **kwargs):
        '''
        Add filled polygons to :class:`matplotlib.axes.Axes` object.

        This method is a wrapper of :meth:`~matplottheme.style.default.Style.fill_betweenx`
        with modifications on the design.

        Notable modification on input argument is

        - ``grid`` is set to ``'both'`` by default.

        .. seealso::
           :meth:`~matplottheme.style.default.Style.fill_betweenx` for documentation on valid kwargs.

        '''
        kwargs.setdefault('grid', 'both')

        result = Style.fill_betweenx(self, ax, y, x1, *args, **kwargs)

        self._post_process(ax)

        return result

    def _grid(self, plot_type, ax, grid, *args, **kwargs):
        # Call MPL API
        ax.grid(axis=grid, color='white', linestyle='-', linewidth=0.5)

    def _post_process(self, ax):
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.patch.set_facecolor(self.palette.frame_bgcolor)
        ax.tick_params(bottom='off', left='off')
