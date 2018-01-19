<template>
  <iu-toolbar-nav searchBox hiddenTitle>
      <v-icon large slot="title">home</v-icon>
      <!-- <span class="hidden-xs-only">Dshop</span> -->
    <!-- <v-avatar size="40px"
          slot="title">
          <img src="src/assets/search.jpg">
    </v-avatar> -->
    <div class="d-flex align-center"
      style="margin-left: auto">
      <Notifications></Notifications>
      <MyShop></MyShop>
    </div>
  </iu-toolbar-nav>
</template>

<script>
import Notifications from './Notifications'
import MyShop from './MyShop'

export default {
  data() {
    return {
      search: ''
    }
  },
  components: {
    Notifications,
    MyShop
  }
}
</script>
