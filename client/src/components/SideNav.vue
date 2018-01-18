<template>
  <v-navigation-drawer fixed
    app
    :value="value"
    @input="value => $emit('input', value)"
    light>
    <v-card flat>
      <v-card-media src="src/assets/logo.png"
        height="100px">
      </v-card-media>
      <v-divider></v-divider>
      <v-list>
        <template v-for="(item, i) in items">
          <v-list-group v-if="item.children"
            v-model="item.model"
            no-action
            :key="i">
            <v-list-tile slot="item">
              <v-list-tile-action>
                <v-icon v-if="item.icon">{{ item.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ item.text }}
                </v-list-tile-title>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-icon>keyboard_arrow_down</v-icon>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile v-for="(child, i) in item.children"
              :key="i"
              @click="$router.push(child.path)">
              <v-list-tile-action>
                <v-icon></v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ child.text }}
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-group>
          <v-list-tile v-else
            @click="$router.push(item.path)"
            :key="i">
            <v-list-tile-action>
              <v-icon v-if="item.icon">{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-card>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['items', 'value'],
  computed: {},
  data() {
    return {}
  }
}
</script>

<style>
/* #keep main .container {
  height: 660px;
} */
/* .navigation-drawer__border {
  display: none;
} */
/* .text {
  font-weight: 400;
}
*/
/* .list__tile__title {
  font-weight: 600;
} */
</style>