<template>
    <iu-toolbar-nav searchBox>
      <template slot="title">
        <v-btn flat large>
      <v-icon  left large>home</v-icon>D쇼핑
        </v-btn>
      <!-- <span class="hidden-xs-only">Dshop</span> -->
      </template>
      <!-- <v-avatar size="90px"
          slot="title">
          <img slot="title" src="src/assets/shopping_search_logo.jpg">
      </v-avatar> -->
      <div class="d-flex align-center" style="margin-left: auto">
           <v-btn flat icon>
    <v-badge top
      color="green">
      <span slot="badge">6</span>
      <v-icon>shopping_cart</v-icon>
    </v-badge>
  </v-btn>
        <v-btn flat>
          <v-icon>perm_identity</v-icon>My Shop
        </v-btn>
      </div>
    </iu-toolbar-nav>
</template>

<script>
export default {
  data() {
    return {
      search: ''
    }
  }
}
</script>
