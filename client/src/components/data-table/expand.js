export default {
  name: 'TableExpand',
  functional: true,
  props: {
    row: Object,
    render: Function,
    column: {
      type: String,
      default: ''
    }
  },
  render(createElement, ctx) {
    const params = {
      row: ctx.props.row
    }
    if (ctx.props.column) params.column = ctx.props.column
    return ctx.props.render(createElement, params)
  }
}
