<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { reactiveOmit } from "@vueuse/core";
import { Separator, type SeparatorProps } from "reka-ui";
import { cn } from "~/lib/utils";

const props = withDefaults(
  defineProps<SeparatorProps & { class?: HTMLAttributes["class"] }>(),
  {
    orientation: "horizontal",
    decorative: true,
  },
);

const delegatedProps = reactiveOmit(props, "class");
</script>

<template>
  <Separator
    v-bind="delegatedProps"
    :class="
      cn(
        'shrink-0 bg-border',
        props.orientation === 'horizontal' ? 'h-px w-full' : 'w-px h-full',
        props.class,
      )
    "
  />
</template>
