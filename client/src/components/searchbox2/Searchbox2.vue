<template>
  <span>
    <input type="search"
      :class="classes"
      :style="styles"
      :placeholder="text"
      autocomplete="off"
      :autofocus="autofocus"
      :value="value"
      @input="updateValue($event.target.value)"
      @focus="onFocus"
      @focusout="onFocusOut"
      @keyup.enter="() => $emit(targetEvent, 'enter')"
      ref="input">
  </span>
</template>

<script scoped>
export default {
  props: {
    focusout: Boolean,
    autofocus: Boolean,
    text: {
      type: String,
      default: '찾기...'
    },
    targetEvent: {
      type: String,
      default: 'onEvent'
    },
    value: {
      type: String,
      default: ''
    },
    width: {
      type: String,
      default: '270px'
    }
  },
  data() {
    return {
      isOpen: false
    }
  },
  computed: {
    classes() {
      return {
        'search-text': true,
        'search-focus': this.isOpen
      }
    },
    styles() {
      return {
        width: this.isOpen ? `${this.width}` : '0px'
      }
    }
  },
  methods: {
    onFocus() {
      this.$emit(this.targetEvent, 'open')
      this.isOpen = true
    },
    onFocusOut() {
      this.$emit(this.targetEvent, 'close')
      if (this.focusout) {
        this.isOpen = false
      }
    },
    updateValue(value) {
      this.$refs.input.value = value.trim()
      this.$emit('input', this.$refs.input.value)
    }
  }
}
</script>

<style scoped>
input.search-text {
  color: #222;
  position: relative;
  z-index: 5;
  -webkit-transition: z-index 0.8s, width 0.5s, background 0.3s ease,
    border 0.3s;
  transition: z-index 0.8s, width 0.5s, background 0.3s ease, border 0.3s;
  height: 45px;
  width: 0;
  margin: 0;
  padding: 5px 0 5px 40px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  font-size: 16px;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 30px;
  border: 1px solid transparent;
  background: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDUxMiA1MTIiIGhlaWdodD0iNTEycHgiIGlkPSJMYXllcl8xIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEycHgiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxwYXRoIGQ9Ik01MDMuODY2LDQ3Ny45NzRMMzYwLjk1OCwzMzUuMDUyYzI4LjcyNS0zNC41NDQsNDYuMDE3LTc4LjkxMiw0Ni4wMTctMTI3LjMzNiAgYzAtMTEwLjA4NC04OS4yMjctMTk5LjMxMi0xOTkuMzEyLTE5OS4zMTJDOTcuNTk5LDguNDAzLDguMzUxLDk3LjYzMSw4LjM1MSwyMDcuNzE1YzAsMTEwLjA2NCw4OS4yNDgsMTk5LjMxMiwxOTkuMzEyLDE5OS4zMTIgIGM0OC40MzUsMCw5Mi43OTItMTcuMjkyLDEyNy4zMzYtNDYuMDE3bDE0Mi45MDgsMTQyLjkyMkw1MDMuODY2LDQ3Ny45NzR6IE0yOS4zMzEsMjA3LjcxNWMwLTk4LjMzNCw3OS45ODctMTc4LjMzMiwxNzguMzMyLTE3OC4zMzIgIGM5OC4zMjUsMCwxNzguMzMyLDc5Ljk5OCwxNzguMzMyLDE3OC4zMzJzLTgwLjAwNywxNzguMzMyLTE3OC4zMzIsMTc4LjMzMkMxMDkuMzE4LDM4Ni4wNDcsMjkuMzMxLDMwNi4wNSwyOS4zMzEsMjA3LjcxNXoiIGZpbGw9IiMzNzQwNEQiLz48L3N2Zz4=)
    no-repeat left 9px center transparent;
  background-size: 20px;
}

input.search-focus {
  z-index: 3;
  border: 1px solid rgb(65, 167, 65);
  background-color: white;
  outline: none;
  cursor: auto;
  padding-right: 10px;
}
/* 
input.search-text::-webkit-search-cancel-button {
  cursor: pointer;
} */
</style>
